import asyncio
import websockets

async def echo(websocket):
	async for message in websocket:
		print("Echoing message '",message,"' now...")
		await websocket.send(message)

async def main():
	async with websockets.serve(echo, "localhost", 8080):
		await asyncio.Future() #run forever

asyncio.run(main())
