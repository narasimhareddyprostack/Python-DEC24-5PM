enames={'Rahul','Sonai','Priyanka'}
fs=frozenset(enames)
print(enames)
print(fs)

enames.add('Modi')  #{'Rahul','Modi','Sonai','Priyanka'}
print(enames)
fs.add('Modi')  #AttributeError
#frozenSet - Immutable Object