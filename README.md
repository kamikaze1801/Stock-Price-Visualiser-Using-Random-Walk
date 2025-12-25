# Stock-Price-Visualiser-Using-Random-Walk

## **Understanding**
This project uses the concept of Random Walk to aids in understanding the range of future possibilities of a stock. A simple experiment to understand the concept of Random Walk is to imagine you are standing at a street corner and flipping a coin. Heads = step forward and Tails = step back. Since each flip is independent and unpredictable of each other, after about 100 flips, you do not know where you would be. This analogy is taken into the pricing of stocks. They move up and down based on random new, economic events and investor sentiment that cannot usually be predicted in advance. 
This project also makes use of the Markov Property which says that the future depends only on the present (+ a shock factor), not on the past. The assumption for this is the efficient market hypothesis. 

### **Why was Daily Returns used?**
Prices were not used for scale problems as different stocks trade at different prices, making it hard to do a fair comparison. Additionally, raw prices are not multiplicative (10% gain followed by 20% gain does not add up to 30% total). Daily returns solves these problems and also provides the benefit of stationarity where these returns typically oscillate around the mean. 
This is done for both the historical prices and forecasted prices to capture real market behaviour. 

### **Mean and Standard Deviation**
Mean is used to understand the drift or trend of the stock (positive or negative). Standard deviation measures the volatility of the stock historically, which can be used to understand the possibilities of its future.

#### _**TLDR;**_
_We use the historical returns to determine the standard deviation. This is then used to forecast future prices. This random walk approach doesn't predict where the stock goes—it shows the range of possibilities and inherent randomness._
