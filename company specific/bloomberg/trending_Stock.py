# https://leetcode.com/discuss/interview-question/627139/Bloomberg-or-Onsite-or-Trending-Stock

from collections import deque

class Stocks:
    def __init__(self):
        self.stocks = {}
        # end is most recently used, start is least recently used
        self.freq_bins = {}
        self.max_freq = 0

    def processStock(self, stock):
        # if stock not in cache, add it to the stock list and to the freq_bin
        if stock not in self.stocks: 
          self.stocks[stock] = 1
          self.freq_bins[1] = self.freq_bins.get(1, deque())
          self.freq_bins[1].append(stock)


          if self.max_freq == 0: self.max_freq += 1

        # if stock in cache
        else:  
          # update the freq in the cache
          freq = self.stocks[stock]
          self.stocks[stock] = freq + 1
          

          # move the stock to the next freq bin
          self.freq_bins[freq].remove(stock)
          
          self.freq_bins[freq+1] = self.freq_bins.get(freq+1, deque())
          self.freq_bins[freq+1].append(stock)
          
          # update max if necessary
          if freq + 1 > self.max_freq:
            self.max_freq += 1
                
        
    def decrementTrendingStock(self):
      # find max freq stock
      max_freq_most_recent_stock = self.freq_bins[self.max_freq].pop()

      # update val in stocks list
      self.stocks[max_freq_most_recent_stock] -= 1

      # move to different freq_bin  
      self.freq_bins[self.max_freq - 1].append(max_freq_most_recent_stock)

      # update max_freq if necessary
      if len(self.freq_bins[self.max_freq]) == 0:
        self.max_freq -= 1 