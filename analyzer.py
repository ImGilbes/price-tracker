import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import sys

vendor = ""
vendor_list = ["amz", "ebay", "zalando"]
if len(sys.argv) > 1:

    if sys.argv[1] in vendor_list:
        vendor = sys.argv[1]
    else:
        print(f"\n---The specified vendor must be among the following:{vendor_list}")
        exit(0)
else:
    print("\n ----You have not specified which vendor to use!----\n")
    exit(0)


sns.set_style("whitegrid")
fig, ax = plt.subplots(figsize=(5, 5))

lastprice = dict()
mean = dict()
var = dict()

path_of_the_directory= './tracked'
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):
        df=pd.read_csv(f)

        titles = filename.split('-') #titles[0] is the title, titles[1] is thw subtitle

        lastprice[titles[0]] = df["price"].iloc[-1]
        mean[titles[0]] = df["price"].mean()
        var[titles[0]] = df["price"].var()

        sns.lineplot(x = "date", y = "price", label = titles[0] , data = df, ax=ax)

for obj in mean.keys():
    printstr = f"- Article: {obj}, price: {lastprice[obj]:.2f}, mean: {mean[obj]:.2f}, variance: {var[obj]:.2f} \n"
    # printstr = printstr + f"price - mean"
    v = lastprice[obj] - mean[obj]
    p = ((v / mean[obj])*100)
    if v < 0:
        printstr = printstr + f"The article is discounted by {abs(v):.2f} euros ({abs(p):.2f}%)\n"
    elif v > 0:
        printstr = printstr + f"the price is currently HIGHER than its average by {abs(v):.2f} euros ({abs(p):.2f}%)\n"
    else:
        printstr = printstr + f"the price is the same as the average (0% discount)\n"
    print(printstr)

plt.show()
