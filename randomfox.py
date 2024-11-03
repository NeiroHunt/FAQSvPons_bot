import aiohttp
import asyncio

# Асинхронная функция для получения случайного изображения лисы
async def fox():
    url = 'https://randomfox.ca/floof/'
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('image')
                else:
                    print(f"Ошибка: {response.status}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    return None

# Тестирование функции
if __name__ == '__main__':
    async def main():
        fox_image = await fox()
        if fox_image:
            print(f'Случайное изображение лисы: {fox_image}')
        else:
            print('Не удалось получить изображение лисы.')

    asyncio.run(main())
