# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class DynamicToken(gl.Contract):

    balances: TreeMap[Address, u256]

    def __init__(self):
        pass

    @gl.public.write
    def mint(self, amount: u256) -> None:
        user = gl.message.sender_address

        current = self.balances.get(user, u256(0))
        self.balances[user] = current + amount

    @gl.public.view
    def my_balance(self) -> u256:
        user = gl.message.sender_address
        return self.balances.get(user, u256(0))
