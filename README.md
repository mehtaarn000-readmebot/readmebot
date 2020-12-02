# readmebot
The cronjob that finds repositories without a README file and submits a PR to add one.

## Inspiration
I've seen a lot a repositories that don't have a README file either because the owner is lazy, or just forgot to add one. 

So, I made this cronjob that finds random repositories, checks whether or not they have a README file, and if not, opens a PR to add one.

## Details
The job runs at 12:00 PM CST everyday.

The PR includes:
- The repo name as the main header
- The description underneath the header
- Installation template
- Dependancies template
- Usage template
- How to contribute template

## Contributing
It's easy to contribute to this repo. Just fork it, add your contributions, and submit a PR with your forked branch.

## Self-Promotion
I am owned by [mehtaarn000](https://github.com/mehtaarn000), so feel free to check out his repositories.

## License
This repository is licensed under the [MIT License](https://opensource.org/licenses/MIT).
