import pandas as pd
#import re

def import_moneywell_transaction_details_file(file_path):
    with open(file_path) as fp:
        is_first_line = True
        transactions_list = []
        transactions = pd.DataFrame(columns=['Payee','Memo','Date','Type','Reference','Amount','Currency'])
        for line in fp:
            print(line)
            parts = line.split('\t')    # re.split(r'\t+', line.rstrip('\t'))
            print(len(parts))
            if is_first_line:
                '''Skip header'''
                is_first_line = False
            else:
                if len(parts[1])+len(parts[2])+len(parts[3])+len(parts[4]) > 0:
                    transactions.loc[len(transactions)+1] = parts
                else:
                    transactions['Category'] = parts[0]
                    transactions_list.append(transactions)
                    transactions = pd.DataFrame(
                        columns=['Payee', 'Memo', 'Date', 'Type', 'Reference', 'Amount', 'Currency'])
        return pd.concat(transactions_list)


if __name__ == '__main__':
    file_path = '201707_Detail.txt'
    imported_transactions = import_moneywell_transaction_details_file(file_path)
    print(imported_transactions)