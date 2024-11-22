fn change(global_state: &mut u32) {
    *global_state +=1
}

fn main() {
    let mut global_state = 0u32;
    println!("initial state: {}", global_state);
    change(&mut global_state);
    println!("final state: {}", global_state);
}
