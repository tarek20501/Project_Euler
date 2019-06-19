#include <stdio.h>

int isPrime(int n){
	if (n == 0 | n == 1)
		return 0;
	if (n == 2)
		return 1;
	for (int i = 2; i < n; i++) {
		if (n%i == 0)
			return 0;
	}
	return 1;
}

unsigned long long int sum_primes_below(unsigned int n) {
	unsigned int i = 0;
	unsigned long long int summ = 0;
	while (i<n){
		if (isPrime(i) == 1){
			summ += i;
			//printf("%u\t%llu\n", i, summ);
		}
		i++;
	}
	printf("%llu\n", summ);
	return summ;
}

void main() {
	sum_primes_below(2000000);
	getchar();
}

//output 142913828922
