# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:35:12 2020

@author: chiji
"""

def solution(N, K):
    # write your code in Python 3.6
    #This function finds the smallest number of rounds of game necessary for a winner 
    # to leave the casino with N-chips having played all-in no more than K times
    #assuming winner won all his game
    
    #Winner can bet All-in  (all chips) to win 2times all he bet or looose all betted
    #Winner can also bet 1 chip to win 2 chips
    
    
    n_rounds = 1#Total number of rounds both adding all and adding just 1 (numi + numj)
    
    addi = 1#Additions of cards or number of current cards
    numi = 0#Number of 1-card win
    numj = 0#number of all-card wins
    #ks = 0
    
    #A function to check if N is less than or equal to 2
    def cont_add():
        #only continue running if N is greater than 2
        
        return N>2
    
    #Check if number of all-in rounds reached a threshhold
    def chek_k():
        #
        return numj>=K
    
    def check_odd(N):
        #Checks if the number is odd number.
        
        return (N+1)/2 == 0
    
    
    checker = cont_add()#Initialize object of the continue add funtion
    checkK = chek_k()#initialize object of the threshhold function
    IsOdd = check_odd(N)#Initialize isodd
    
    while checker == True:
        
        if (IsOdd == False)  & (checkK == False):
            
            N = N/2#reduce N by half
            #addi += addi
            numj += 1
            #n_rounds = numj+numi
            checker = cont_add()
            checkK = chek_k()
        
        
        else:
            N -= 1#subtract 1 from n
            numi += 1
            checker = cont_add()
            checkK = chek_k()
        
        
    return numi+numj+1