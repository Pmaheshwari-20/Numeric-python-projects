import time, sys

def zeta_accel(exp_s, term_lim):
    if term_lim <= 0:
        return 0.0

    local_pow = pow
    alt_sum = 0.0
    idx = 1
    sign = 1.0
    inv_s = exp_s

    while idx <= term_lim:
        alt_sum += sign / local_pow(idx, inv_s)
        idx += 1
        sign = -sign

    scale = 1.0 / (1.0 - local_pow(2.0, 1.0 - exp_s))
    return alt_sum * scale

start_t = time.time()

exp_s = float(input("Enter s value: "))
term_lim = int(input("Enter number of terms: "))

res_zeta = zeta_accel(exp_s, term_lim)

end_t = time.time()

print("Accelerated ζ(s):", res_zeta)
print("Execution time:", end_t - start_t)

mem_bytes = (
    sys.getsizeof(exp_s) +
    sys.getsizeof(term_lim) +
    sys.getsizeof(res_zeta) +
    sys.getsizeof(start_t) +
    sys.getsizeof(end_t)
)
print("Approx memory used (bytes):", mem_bytes)

