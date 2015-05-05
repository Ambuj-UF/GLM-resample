################################################################################################################
# This program was written for creating running GLM analysis on the unique patterns obtained from the  data    #
# sample of relatedness between parasitic offspring and host mothers obtained by Ye Gong,  Kimball-Brain lab   #
# group, Biology Department, University of Florida}                                                            #
#                                                                                                              #
# Copyright (C) {2014}  {Ambuj Kumar, Kimball-Brain lab group, Biology Department, University of Florida}      #
#                                                                                                              #
# This program is free software: you can redistribute it and/or modify                                         #
# it under the terms of the GNU General Public License as published by                                         #
# the Free Software Foundation, either version 3 of the License, or                                            #
# (at your option) any later version.                                                                          #
#                                                                                                              #
# This program is distributed in the hope that it will be useful,                                              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of                                               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                                                #
# GNU General Public License for more details.                                                                 #
#                                                                                                              #
# This program comes with ABSOLUTELY NO WARRANTY;                                                              #
# This is free software, and you are welcome to redistribute it                                                #
# under certain conditions;                                                                                    #
#                                                                                                              #
################################################################################################################


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

plot(x,y,type="l",lwd=2,col="red")

