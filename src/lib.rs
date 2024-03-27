use pyo3::prelude::*;
use rand::seq::SliceRandom;
use rand::thread_rng;
use pyo3::exceptions;
use std::fs::File;
use std::io::Read;
use serde_json;

#[pyfunction]
fn checking_password_security(password: String) -> PyResult<&'static str> {
    let mut lowercase: bool = true;
    let mut uppercase: bool = true;
    let mut hasnumber: bool = true;
    let mut has_special_char = true;

    if password.len() >= 10 {
        for character in password.chars(){
            if character.is_ascii_lowercase() {
                lowercase = false;
            }
            if character.is_ascii_uppercase() {
                uppercase = false;
            }
            if !character.is_ascii_alphanumeric() {
                has_special_char = false;
            }
            if character.is_numeric() {
                hasnumber = false;
            }
        }
    }
    else {
        return Err(PyErr::new::<exceptions::PyValueError, _>("You're password is not 14 Characters long."));
    }

    if lowercase {
        return Err(PyErr::new::<exceptions::PyValueError, _>("You're password doesn't have lowercase."));
    } else if uppercase {
        return Err(PyErr::new::<exceptions::PyValueError, _>("You're password doesn't have uppercase."));
    } else if has_special_char {
        return Err(PyErr::new::<exceptions::PyValueError, _>("You're password doesn't have any special chars."));
    } else if hasnumber {
        return Err(PyErr::new::<exceptions::PyValueError, _>("You're password doesn't have any numeric value."));
    }
    else {
        return Ok("Password is Valid");
    }
}

#[pyfunction]
fn random_password_generator(length: u8) -> PyResult<String> {
    let mut password1 = String::new();
    let mut password2 = String::new();
    let mut password3 = String::new();

    let file_path = "/Users/dharmikpatel/Desktop/Projects/Password Management System/policy.json";
    let policy: Vec<char> = read_json_file(file_path);

    // let lowercase: Vec<char> = ('a'..='z').collect();
    // let uppercase: Vec<char> = ('A'..='Z').collect();
    // let digits: Vec<char> = ('0'..='9').collect();
    // let punctuation: Vec<char> = "!@#$%^&*()-=_+[]{}|;:,.<>?".chars().collect();
    // let policy: Vec<char> = concat(vec![lowercase, uppercase, digits, punctuation]);
    // let policy: Vec<char> = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-=_+[]{}|:,.<>?".chars().collect();
    
    let mut rng = thread_rng();

    for _i in 0..length {
        password1.push(*policy.choose(&mut rng).unwrap_or(&' '));
        password2.push(*policy.choose(&mut rng).unwrap_or(&' '));
        password3.push(*policy.choose(&mut rng).unwrap_or(&' '));
    }

    let lastpass: Vec<char> = format!("{}{}{}", password1, password2, password3).chars().collect();
    let mut final_password = String::new();
    for _i in 0..length {
        final_password.push(*lastpass.choose(&mut rng).unwrap_or(&' '));
    }

    if checking_password_security(final_password.to_string()).is_ok() {
        Ok(final_password)
    }
    else {
        return Err(PyErr::new::<exceptions::PyValueError, _>("Not Valid"));
    }
}

fn read_json_file(file_path: &str) -> Vec<char> {
    // Open the file and read its contents into a String
    let mut file = File::open(file_path).expect("Unable to open the file");
    let mut file_contents = String::new();
    file.read_to_string(&mut file_contents).expect("Unable to read the file");

    // Parse the JSON data into a MyData structure
    let my_data: serde_json::Value = serde_json::from_str(&file_contents).expect("Unable to parse JSON");

    let policy = my_data.get("policy").expect("file should have FirstName key");

    let final_policy: Vec<char> = policy.as_str().expect("policy should be a string").chars().collect();
    final_policy
}

#[pymodule]
fn Pass_Rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(checking_password_security, m)?)?;
    m.add_function(wrap_pyfunction!(random_password_generator, m)?)?;
    Ok(())
}
