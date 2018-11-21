import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt



pd.set_option('display.max_columns',50)
pd.set_option('display.max_rows',200)


lib = pd.read_csv('BL-Flickr-Images-Book.csv')
#print(list(lib))
print(lib.shape)

lib_rename = lib.rename(index=str, columns={'Identifier': 'id',
                                            'Edition Statement': 'edition_statement',
                                            'Place of Publication': 'publication_place',
                                            'Date of Publication': 'publication_date',
                                            'Publisher': 'publisher',
                                            'Title': 'title',
                                            'Author': 'author',
                                            'Contributors': 'contributors',
                                            'Corporate Author': 'corp_author',
                                            'Corporate Contributors': 'corp_contributors',
                                            'Former owner': 'former_owner',
                                            'Engraver': 'engraver',
                                            'Issuance type': 'issuance_type',
                                            'Flickr URL': 'flickr',
                                            'Shelfmarks': 'shelfmarks'})
#print(list(lib_rename))
#print(lib_rename.head())
#print(lib_rename.tail())

#engraver does not have any values, dropping

lib_rename = lib_rename.drop(columns='engraver')
print('what happened')

print(lib_rename.publisher.unique())
with pd.option_context('display.max_rows', 200, 'display.max_columns', 50):
    print(lib_rename.publisher.unique())



