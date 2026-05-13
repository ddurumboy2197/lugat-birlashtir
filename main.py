def eng_katta_kalit(lugat):
    return max(lugat, key=lugat.get)
```

Kodni ishlatish uchun misol:

```python
lugat = {"a": 5, "b": 10, "c": 3, "d": 20}
print(eng_katta_kalit(lugat))  # Chiqaradi: "d"
