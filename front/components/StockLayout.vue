<template>
    <Layout>
        <template #navbar>
			<div class="flex w-full h-full bg-cyan-800 text-neutral-50">
				<!-- <NuxtLink class="flex items-center justify-center h-full w-fit p-2 font-sans" to="/apps/">Apps</NuxtLink> -->
				<NuxtLink class="flex items-center justify-center h-full w-fit p-2 font-sans" to="/stock/">Склад</NuxtLink>
				<Dropdown group="0" class=" z-10 flex items-center justify-center h-full w-fit p-2 font-sans">
					<template #folded>
						<button class="flex items-center justify-center h-full w-fit p-2 font-sans">Основное</button>
					</template>
					<NuxtLink class="block px-4 py-2 w-fit min-w-full text-black hover:bg-cyan-800 hover:text-neutral-50" to="/stock/location/">Склады</NuxtLink>
					<!-- <NuxtLink class="block px-4 py-2 w-fit min-w-full text-black hover:bg-cyan-800 hover:text-neutral-50" to="/stock/move/">История перемещений</NuxtLink> -->
				</Dropdown>
			</div>
		</template>
      <slot />
    </Layout>
  </template>