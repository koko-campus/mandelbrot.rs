extern crate image;

use std::fs::File;
use std::str::FromStr;
use std::io::Write;
use num::Complex;
use image::ColorType;
use image::png::PNGEncoder;


fn escape_time(c: Complex<f64>, limit: u32) -> Option<u32> {
    let mut z = Complex{re: 0.0, im: 0.0};
    for i in 0..limit {
        z = z * z + c;
        if 4.0 < z.norm_sqr() {
            return Some(i);
        }
    }
    None
}


fn parse_pair<T: FromStr>(s: &str, separator: char) -> Option<(T, T)> {
    match s.find(separator) {
        None => None,
        Some(index) => {
            match (T::from_str(&s[..index]), T::from_str(&s[index + 1..])) {
                (Ok(l), Ok(r)) => Some((l, r)),
                _ => None
            }
        }
    }
}


fn parse_complex(s: &str) -> Option<Complex<f64>> {
    match parse_pair(s, ',') {
        Some((re, im)) => Some(Complex {re, im}),
        None => None,
    }
}


fn pixel2point_cenverter(bounds: (usize, usize), pixel: (usize, usize), upper_left: Complex<f64>, lower_right: Complex<f64>) -> Complex<f64> {
    let (width, height) = (lower_right.re - upper_left.re, upper_left.im - lower_right.im);
    Complex {
        re: upper_left.re + pixel.0 as f64 * width / bounds.0 as f64,
        im: upper_left.im - pixel.1 as f64 * height / bounds.1 as f64,
    }
}


fn render(pixels: &mut [u8], bounds: (usize, usize), upper_left: Complex<f64>, lower_right: Complex<f64>) {
    for row in 0..bounds.1 {
        for col in 0..bounds.0 {
            let point = pixel2point_cenverter(bounds, (col, row), upper_left, lower_right);
            pixels[row * bounds.0 + col] = match escape_time(point, 255) {
                None => 0,
                Some(count) => 255 - count as u8,
            };
        }
    }
}


fn write_image(filename: &str, pixels: &[u8],bounds: (usize, usize)) -> Result<(), std::io::Error> {
    let file = File::create(filename)?;
    let encoder = PNGEncoder::new(file);
    encoder.encode(&pixels, bounds.0 as u32, bounds.1 as u32, ColorType::Gray(8))?;
    Ok(())
}


fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 5 {
        writeln!(std::io::stderr(), "mandelbrot file_name pixels upperleft lowerright").unwrap();
        std::process::exit(1);
    }

    let bounds = parse_pair(&args[2], 'x').expect("snd param must be \"widthxheight\"");
    let upper_left = parse_complex(&args[3]).expect("3rd param must be \"left corner\"");
    let lower_right = parse_complex(&args[4]).expect("4rd param must be \"left corner\"");

    // let x_ratio = bounds.0 as f64 / (lower_right.im - upper_left.im);
    // let y_ratio = bounds.1 as f64 / (lower_right.re - upper_left.re);
    // println!("{} - {}", x_ratio, y_ratio);
    // if x_ratio != y_ratio {
    //     writeln!(std::io::stderr(), "aspect ratio is not \"1 / 1\"").unwrap();
    //     std::process::exit(1);     
    // }
    // println!(" start !! ");
    println!("filename -> {} | filesize -> {}x{} | upperleft -> {},{} | lowerright -> {},{} |", &args[1], bounds.0, bounds.1, upper_left.re, upper_left.im, lower_right.re, lower_right.im);
    let mut pixels = vec![0; bounds.0 * bounds.1];
    render(&mut pixels, bounds, upper_left, lower_right);
    write_image(&args[1], &pixels, bounds).expect("error while writing PNG file.");
    // println!(" end !! ");
}

