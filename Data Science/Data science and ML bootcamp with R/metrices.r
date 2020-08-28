goog <- c(100,101,102,103,104)
msft <- c(200, 201,202,203,204)


stocks <- c(goog,msft)



stocks.metrix <- matrix(stocks, nrow = 2, byrow = T)
days <- c("Mon", "Tue","Wed", "Thurs","fri")
st.names <- c("goog", "MSFT")

colnames(stocks.metrix)<- days
rownames(stocks.metrix) <- st.names


print(stocks.metrix)


