# ------------------------------------------------------------------------------------------------------------------
# https://stackoverflow.com/questions/739654/how-to-make-function-decorators-and-chain-them-together/1594484#1594484

print("0.Funções sem decorators-----------------------------------------------")


def bread(func):
	def wrapper():
		print("</''''''\>")
		func()
		print("<\______/>")

	return wrapper


def ingredients(func):
	def wrapper():
		print("#tomatoes#")
		func()
		print("~salad~")

	return wrapper


def sandwich(food="--ham--"):
	print(food)


sandwich()
# outputs: --ham--
sandwich = bread(ingredients(sandwich))
sandwich()
# outputs:
# </''''''\>
# #tomatoes#
# --ham--
# ~salad~
# <\______/>

# -----------------------------------------------------------------------------
# Using the Python decorator syntax:
print("1.sandwich with ham: -----------------------------------------------")


@bread
@ingredients
def sandwich(food="--ham--"):
	print(food)


sandwich()
# outputs:
# </''''''\>
# #tomatoes#
# --ham--
# ~salad~
# <\______/>


# -----------------------------------------------------------------------------
# The order you set the decorators MATTERS:
print("2.strange_sandwich[wrong order of decorators]: -----------------------------------------------")


@ingredients
@bread
def strange_sandwich(food="--ham--"):
	print(food)


strange_sandwich()
# outputs:
# #tomatoes#
# </''''''\>
# --ham--
# <\______/>
# ~salad~
