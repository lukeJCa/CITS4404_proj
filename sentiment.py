from textblob import TextBlob

some_headlines = ['Medtronic profit falls nearly 44% as COVID-19 hurts demand Reuters',
                    'XpresSpa Shares Jump Over 18%, As Company Says It Has Expedited Airport COVID-19 Screening Benzinga,'
                    'The Zacks Analyst Blog Highlights: QIAGEN, Merit Medical, OPKO, Abbott and Abiomed Zacks',
                    'The Next Bull Run Will Be Harder For Sorrento Therapeutics InvestorPlace']

for xx in some_headlines:

    testimonial = TextBlob(xx)
    print(testimonial.sentiment)