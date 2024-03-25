<script setup>
	const SuperCell = resolveComponent("SuperCell")
</script>

<template>
	<div class="p-20 w-full h-full">
		<ActionBar>
			<template #header="headerProps">
				<button @click="headerProps.revert_action" class="m-2 p-2 bg-slate-200 border-slate-300 border rounded-md hover:border-slate-500 hover:bg-slate-300 shadow-md active:bg-gray-400">Revert</button>
				<button @click="headerProps.save_action" class="m-2 p-2 bg-slate-200 border-slate-300 border rounded-md hover:border-slate-500 hover:bg-slate-300 shadow-md active:bg-gray-400">Save</button>
			</template>
			<List controllable model="StockMove">
				<Field name="product" :widget="SuperCell" />
				<Field name="quantity" :widget="SuperCell" />
			</List>
		</ActionBar>
	</div>
</template>
