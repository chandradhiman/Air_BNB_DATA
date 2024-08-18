Note {ragarding how this repo works}
1. how to read file 
    
file_path = 'file_name /airbnb_contacts.xlsx'
rank = pd.read
_excel("file_name/airbnb_contacts.xlsx")

2. Pivot table
    an interactive way to quickly summarize large amounts of data
    use for summarize, aggregator and explore data interactively and organized format by rearranging the data, grouping it, and calculating aggregated metrics like sums, averages, counts, etc. 
    eg: pivot = df.pivot_table(values = 'child', index = 'Men', columns= 'Women', aggfunc= 'sum')
    this is a pandas function.
    

