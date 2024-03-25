<script setup>
	const router = useRouter()
	let routes = router.getRoutes()
	routes.forEach((path, index) => {
		if (path.path.includes(":id()") ){
			routes[index].path = path.path.replace(":id()", "1")
			console.log(routes[index].path)
		}
	} )
	console.log(router.getRoutes())
</script>

<template>
	<StockLayout>
		<p>Приложение склада</p>
	</StockLayout>
</template>
