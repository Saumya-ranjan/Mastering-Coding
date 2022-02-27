def func(x):
    count = 0
    a = ""
    for j in x:
        a+=j

    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in a:
            count+=1
    if count == 0:
        print('1')
    else:
        print('0')

func(["jwtucoucmdfwxxqnxzkaxoglszmfrcvjoiunqqausaxxaaijyqdqgvdnqcaihwilqkpivenpnekioyqujrdrovqrlxovcucjqzjsxmllfgndfprctxvxwlzjtciqxgsxfwhmuzqvlksyuztoetyjugmswfjtawwaqmwyxmvo"])