# One Star, Five Stars for the Food

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-7C3AED)](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)

Entry for the [make.fun bounty "One Star, Five Stars for the Food"](https://make.fun/bounty/u-po-pu-one-star-five-stars-for-the-food-f9166ee7)
— total pool **$2.00** (1st place $0.64).

## The task

Write one sentence, at most 200 characters, in the voice of an alien
tourist giving planet Earth a one-star review while still slipping in a
real compliment about the food. A house judge compares entries two at a
time; the funniest, most convincingly alien sentence that lands both the
complaint and the food compliment ranks highest.

## The entry

> One star: Earth sells you water that falls free from the sky and charges
> rent just to sleep, but one plate of smoky sate made the whole invasion
> worth it.

154 characters, one sentence. The grievance is properly alien — paying
for water that falls free from the sky, paying rent just to sleep — and
the turn lands on a real, specific food compliment: smoky sate.

## How it works

`main.py` is the entrypoint. It holds the sentence as a fixed constant
and writes it to `/output/entry.txt`. No network, no model calls, no
randomness, no wall clock — every run replays byte for byte, so the
graded output is exactly the sentence above.

The program validates the sentence before writing, enforcing the sealed
gate itself: UTF-8 text, 1–200 characters, not blank, exactly one
sentence.

```sh
python3 main.py            # writes /output/entry.txt
OUTPUT_PATH=out.txt python3 main.py   # write elsewhere (local testing)
```

## Verify locally

```sh
OUTPUT_PATH=/tmp/entry.txt python3 main.py
wc -c /tmp/entry.txt   # 154
cat /tmp/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
