def read_file(file_name):
    lines = []
    with open(file_name,'r',encoding = 'utf-8-sig') as f:
         for line in f:
         	lines.append(line.strip())
    return lines


def convert(lines):
    Allen_words_count = 0
    Allen_stickers_count = 0
    Allen_images_count = 0
    Viki_words_count = 0
    Viki_stickers_count = 0
    Viki_images_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            for m in s[2:]:
                if m == '貼圖':
                    Allen_stickers_count += 1
                elif m == '圖片':
                    Allen_images_count += 1    
                else:    
                    Allen_words_count += len(m)
        elif name == 'Viki':
            for m in s[2:]:
                if m == '貼圖':
                    Viki_stickers_count += 1
                elif m == '圖片':
                    Viki_images_count += 1    
                else:    
                    Viki_words_count += len(m)
    print('Allen 說了', Allen_words_count, '個字')
    print('Allen 傳了', Allen_stickers_count, '張貼圖')
    print('Allen 傳了', Allen_images_count, '張圖片')
    
    print('Viki 說了', Viki_words_count, '個字')
    print('Viki 傳了', Viki_stickers_count, '張貼圖')
    print('Viki 傳了', Viki_images_count, '張圖片')


def write_file(file_name,lines):
    with open (file_name,'w',encoding = 'utf-8') as f:
        for line in lines:
        	f.write(line + '\n')
    return f


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)  
    #write_file('output.txt',lines) 


main()