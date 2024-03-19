# Fabrica

> ...

![img1](media/img1.jpg)
![img2](media/img2.jpg)
![img3](media/img3.jpg)
![img5](media/img5.jpg)
![img4](media/img4.jpg)
**Dastur ishlashining misoli.**


## `Endpoints:`
- `POST` → `…/api/add`  
### `Request:`
```json
{
  "products": [
    {"product_name": "Koylak", "product_qty": 30},
    {"product_name": "Shim", "product_qty": 20}
  ]
}
```

### `Response:`
```json
{
    "result": [
        {
            "product_name": "Koylak",
            "product_qty": 30,
            "product_materials": [
                {
                    "material_name": "Mato",
                    "qty": 12,
                    "warehouse_id": 19,
                    "price": 1500.0
                },
                {
                    "material_name": "Mato",
                    "qty": 12.0,
                    "warehouse_id": 20,
                    "price": 1600.0
                },
                {
                    "material_name": "Tugma",
                    "qty": 150.0,
                    "warehouse_id": 23,
                    "price": 300.0
                },
                {
                    "material_name": "Ip",
                    "qty": 40,
                    "warehouse_id": 21,
                    "price": 300.0
                },
                {
                    "material_name": "Ip",
                    "qty": 260.0,
                    "warehouse_id": 22,
                    "price": 550.0
                }
            ]
        },
        {
            "product_name": "Shim",
            "product_qty": 20,
            "product_materials": [
                {
                    "material_name": "Mato",
                    "qty": 28.0,
                    "warehouse_id": 20,
                    "price": 1600.0
                },
                {
                    "material_name": "Ip",
                    "qty": 40.0,
                    "warehouse_id": 22,
                    "price": 550.0
                },
                {
                    "material_name": "Ip",
                    "qty": 260.0,
                    "warehouse_id": null,
                    "price": null
                },
                {
                    "material_name": "Zamok",
                    "qty": 20.0,
                    "warehouse_id": 24,
                    "price": 2000.0
                }
            ]
        }
    ]
}
```


