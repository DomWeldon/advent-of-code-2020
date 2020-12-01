use itertools::Itertools;


// generator to parse first day's input
#[aoc_generator(day1)]
pub fn parse_ints(input: &str) -> Vec<u64> {
    // it's just a list of lines
    let result = input.split_whitespace()
        .map(|l| l.parse().unwrap())
        .collect::<Vec<u64>>();
    result
}

fn find_sum_product(input: &[u64], target: u64, n: usize) -> Option<u64> {
    let combinations = input.iter().combinations(n);
    for t in combinations {
        let tot: u64 = t.iter().fold(0, |acc, &v| acc + v);
        if tot == target {
            return Some(t.iter().fold(1, |acc, &v| acc * v));
        }
    }

    None
}

#[aoc(day1, part1)]
pub fn part1(input: &[u64]) -> u64 {
    let p = find_sum_product(input, 2020, 2).unwrap();

    p
}

#[aoc(day1, part2)]
pub fn part2(input: &[u64]) -> u64 {
    let p = find_sum_product(input, 2020, 3).unwrap();

    p
}
