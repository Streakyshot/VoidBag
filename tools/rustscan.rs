// rustscan.rs - Pro Tool: Basic TCP Port Scanner in Rust
use std::net::TcpStream;
use std::time::Duration;
use std::env;

fn main() {
    println!("[*] RustScan: TCP Port Scanner");
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        println!("Usage: rustscan <ip>");
        return;
    }

    let ip = &args[1];
    for port in 1..1025 {
        let addr = format!("{}:{}", ip, port);
        if let Ok(_) = TcpStream::connect_timeout(&addr.parse().unwrap(), Duration::from_millis(100)) {
            println!("[+] Open: {}", port);
        }
    }
}
