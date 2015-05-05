require(ggplot2)
require(sandwich)
require(msm)


pvalue <- c()
rVal <- c()

for (x in 0:9999) {
    p <- read.csv(paste("excellData/pattern", toString(x), ".csv", sep=""))
    colnames(p) <- c("sib", "offnum", "year", "fid", "relatedness")
    p <- within(p, {fid <- factor(fid)
        year <- factor(year)
    })

    pval <- summary(m1 <- glm(offnum ~ year + fid + relatedness, family="poisson", data=p))
    pvalue <- c(pvalue, pval[12]$coefficient[length(pval[12]$coefficient)])
    relat <- coef(m1)
    rVal <- c(rVal, relat[length(relat)])
    
}


print(sort(pvalue))
cat("\n\n")
print(sort(rVal))

x <- sort(pvalue)

y=dnorm(x,mean=mean(x),sd=sd(x))

plot(x,y,type="l",lwd=2,col="black", xlab = "P value", ylab = "Dnorm of p values")


x <- sort(rVal)
y=dnorm(x,mean=mean(x),sd=sd(x))
plot(x,y,type="l",lwd=2,col="black", xlab = "Relatedness", ylab = "Dnorm of relatedness")