# Educators — ALAVETELI

**Project:** ALAVETELI  
**Category:** GOVERNMENT  
**Upstream:** https://github.com/mysociety/alaveteli  
**Pinned commit:** `6ad79e9334c4131078c6a67560452bfd5e7781b8`  
**Assurance:** 16/16 checks passing  
**Ledger head:** `f2daaf2a0f1103b1b92be7c0b85cb07ec7cca312093eaa1d7392785bb22e5874`  
**Date:** October 2026

## Teaching with ALAVETELI

The project is usable as a worked example of offline-first packaging with a
cryptographic audit chain. It ships with the assurance suite, the evidence
register and the ledger, so students can verify claims rather than take them on
faith.

## Suggested exercises

1. Run `python tools/run_bench.py --out BENCH.json` and read the 16 results.
2. Recompute the SHA3-256 of a row's evidence file and compare to the register.
3. Walk the AIOSS chain from genesis to head `f2daaf2a0f1103b1b92be7c0b85cb07ec7cca312093eaa1d7392785bb22e5874` and confirm every link.
4. Break one artifact and observe the chain fail to verify.

## Licence for teaching

Apache 2.0 terms apply to academic and teaching use. See `24_ANTICOMMONS_LICENSE`.
