def total_carrito(request):
    total = 0
    total_items = 0
    service = False
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            try:
                if value["cantidad"]:
                    print('Es un producto')
            except:
                service = True
                print('Es un servicio')
            total += int(value["acumulado"])
            total_items += 1
    return {"total_carrito": total, "total_items": total_items, "service": service}