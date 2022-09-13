extern crate image;

use std::fs::File;
use num;
use num::bigint::BigInt;
use num::rational::{Ratio, BigRational};
use image::ColorType;
use image::png::PNGEncoder;



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
    let file = File::create(filename);
    let encoder = PNGEncoder::new(file);
    encoder.encode(&pixels, bounds.0 as u32, bounds.1 as u32, ColorType::Gray(8))?;
    Ok(())
}


fn main() {
    println!("Hello, world!");
}

