# Diskretni rozdeleni
## Binomicke rozdeleni: n - pocet pokusu, p - pst uspechu
```r
# pocet uspechu v n-pokusech
pbinom(k,n,p) # - distribucni funkce
dbinom(k,n,p) # - pravdepodobnostni funcke
n*p # stredni hodnota 
n*p*(1-p) # rozptyl 
```

## Hypergeometricke rozdeleni: w - pocet bilych kouli v osudi, b - pocet cernych kouli v osudi
```r
n # - pocet kouli tazenych z osudi
# pocet bilych kouli mezi n tazenymi
phyper(k,w,b,n) # - distribucni funkce
dhyper(k,w,b,n) # - pravdepodobnostni funcke
n*w/(w+b) # stredni hodnota 
(n*w/(w+b))*(1-w/(w+b))*((w+b-n)/(w+b-1)) # rozptyl 
```

## Geometricke rozdeleni: p - pravdepodobnost uspechu
```r
# cekani na prvni uspech, do prikazu se zadava pocet neuspechu pred prvnim uspechem
pgeom(k,p) # - distribucni funkce
dgeom(k,p) # - pravdepodobnostni funcke
(1-p)/p # - stredni hodnota 
(1-p)/p^2 # - rozptyl 
```


## Poissonovo rozdeleni: lambda - stredni hodnota
```r
# pocet udalosti
 ppois(k,lambda) # - distribucni funkce
 dpois(k,lambda) # - pravdepodobnostni funcke
# stredni hodnota lambda
# rozptyl lambda
```

## Negativni binomicke rozdeleni: n - pocet uspechu, p - pst uspechu
```r
 pnbinom(k,n,p) # - distribucni funkce
 dnbinom(k,n,p) # - pravdepodobnostni funcke
```

# Spojita rozdeleni
## Normalni rozdeleni: mu - stredni hodnota, sigma - smerodatna odchylka
```r
pnorm(x,mu,sigma) # - distribucni funkce
```