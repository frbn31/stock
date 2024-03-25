<script setup>
	const SuperCell = resolveComponent("SuperCell")
</script>

<template>
	<StockLayout>
		<div class="p-20 w-full h-full">
		<ActionBar>
			<template #header="headerProps">
				<button @click="headerProps.revert_action" class="m-2 p-2 bg-slate-200 border-slate-300 border rounded-md hover:border-slate-500 hover:bg-slate-300 shadow-md active:bg-gray-400">Revert</button>
				<button @click="headerProps.save_action" class="m-2 p-2 bg-slate-200 border-slate-300 border rounded-md hover:border-slate-500 hover:bg-slate-300 shadow-md active:bg-gray-400">Save</button>
			</template>
			<Card model="StockLocation" padded creation controllable>
				<template v-slot:header>
					<p class="m-2 bg-slate-100">Bruh</p>
					<p class="m-2 bg-slate-100">Bruh</p>
					<p class="m-2 bg-slate-100">Bruh</p>
					<p class="m-2 bg-slate-100">Bruh</p>
					<p class="m-2 bg-slate-100">Bruh</p>
				</template>
				<template v-slot:button-box>
				</template>
				<template v-slot:main-info>
					<CardGroup>
						<CardField name="name" alias="наименование" />
					</CardGroup>
				</template>
				<template v-slot:tabs>
					<Tabs>
						<Tab title="Tab 1">Tab 1 Content</Tab>
						<Tab title="Tab 2">Tab 2 Content</Tab>
						<Tab title="Tab 3">Tab 3 Content</Tab>
						<Tab title="Tab 4">Tab 4 Content</Tab>
					</Tabs>
				</template>
			</Card>
		</ActionBar>
	</div>
	</StockLayout>
	
</template>
