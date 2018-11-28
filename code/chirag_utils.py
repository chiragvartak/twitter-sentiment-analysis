import csv
import pandas as pd

RAW_FILE_PATH="/Users/chirag.vartak/learn/twitter-sentiment-analysis/dataset/training.1600000.processed.noemoticon.csv"
TRIMMED_FILE_PATH="/Users/chirag.vartak/learn/twitter-sentiment-analysis/dataset/trimmed_file.csv"
FINAL_CSV_PATH="/Users/chirag.vartak/learn/twitter-sentiment-analysis/dataset/final.csv"
LAST_CSV_PATH="/Users/chirag.vartak/learn/twitter-sentiment-analysis/dataset/last.csv"

def process_twitter_dataset_csv(file_path):
    file = open(file_path)
    with open(file_path, "r") as source:
        rdr = csv.reader(file)
        with open(FINAL_CSV_PATH, "w") as result:
            wtr = csv.writer(result)
            for r in rdr:
                wtr.writerow((r[0], r[1], r[5]))

def process_twitter_dataset_csv_2():
    final_csv = open(FINAL_CSV_PATH, "r")
    df = pd.read_csv(final_csv)
    columnsTitles = ["sentiment", "id", "tweet"]
    df = df.reindex(columns=columnsTitles)
    print(list(df))
    df2 = df[["id", "sentiment", "tweet"]]
    print(list(df2))
    with open(LAST_CSV_PATH, "w") as output:
        df2.to_csv(LAST_CSV_PATH)
    final_csv.close()

# Equal number of positive, negative, and neutral lines
def trim_file(file_path, number_of_lines):
    positives = number_of_lines // 3
    negatives = positives
    neutrals = number_of_lines - positives - negatives
    with open(RAW_FILE_PATH, "r") as input_file:
        with open(TRIMMED_FILE_PATH, "w") as output_file:
            try:
                for i,line in enumerate(input_file):
                    # print(line[1], end="")
                    if line[1] == "0":
                        if negatives <= 0:
                            continue
                        output_file.write(line)
                        negatives -= 1
                    elif line[1] == "2":
                        if neutrals <= 0:
                            continue
                        output_file.write(line)
                        neutrals -= 1
                    elif line[1] == "4":
                        if positives <= 0:
                            continue
                        output_file.write(line)
                        positives -= 1
                    else:
                        print ("Invalid character: " + line[1])
            except UnicodeDecodeError:
                print("UnicodeDecodeError on line " + str(i) + ", ignoring this line")


if __name__ == "__main__":
    # trim_file(RAW_FILE_PATH, 9000)
    process_twitter_dataset_csv(TRIMMED_FILE_PATH)
    process_twitter_dataset_csv_2()