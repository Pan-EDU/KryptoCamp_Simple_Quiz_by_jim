# 進擊的韭菜 solution by Python

###### tags: `KryptoCamp`

[TOC]

## How to run

```bash=1
$ cat input.txt
# 5
# 3
# 1 3
# 3 5
# 1 5
$ python3 solution.py
# 4
```

## How do I think

### 題目描述釐清

題目的描述中，「割韭菜」有賣出與買入兩種形式。而後續提及起始狀態為「韭菜手上都持有比特幣」，而接下來「會有 M 次割韭菜的行為」，並最後目標要知道「有多少韭菜還沒有賣掉比特幣」。

但從範例中得知，最後目標的敘述應該為「知道最後有多少韭菜身上具有比特幣」較為精確。

理由如下：

```
1 2 3 4 5
-----
    -----
---------
```

上圖中的 `12345` 為`所有韭菜`的編號，而 `-` 所涵蓋的區域則是遭遇割韭菜事件的範圍。若題目欲得知的是「從未賣掉比特幣」之韭菜數，範例輸出應該為0。故從`4`的結果推斷，最後預期的輸出為「最後有多少韭菜身上具有比特幣」。

### 題目解法

從範例輸入可明確可出，只要知道「受割」次數的奇偶數，即可判斷其是否仍擁有比特幣。目標變成找出「受割次數是偶數」的韭菜數。

在 Python 實作中就以單純的 List 去進行篩選，很快就能知道奇偶數分別的數量。