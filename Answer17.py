"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage."""


initDict1 = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
             11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
             18: "Eighteen", 19: "Nineteen",
             10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty",
             90: "Ninety", 100: "Hundred", 1000: "Thousand"}
for num in range(1, 1001):
        if num < 101:
            if num not in initDict1:
                newNum = num // 10 * 10
                initDict1[num] = initDict1[newNum] + initDict1[num % 10]
                # print(num, " : ", initDict1[newNum] + initDict1[num % 10])
        elif num < 1000:
            newNum = num // 100
            newNum1 = (newNum * 100) // newNum
            if num % 100 != 0:
                initDict1[num] = initDict1[newNum] + initDict1[newNum1] + 'And' + initDict1[num % 100]
                # print(num, " : ", initDict1[newNum] + initDict1[newNum1] +'And'+ initDict1[num % 100])
            else:
                initDict1[num] = initDict1[newNum] + 'And' + initDict1[newNum1]
                # print(num, " : ", initDict1[newNum] + 'And' +initDict1[newNum1])

wordCount = 0
for num in initDict1.values():
    wordCount += len(num)
print(wordCount)


