<script>
    import { newPosts } from "../../stores/postStore.js";
    import PostItem from "../shared/PostItem.svelte";
</script>

<style>
</style>

<svelte:head>
    <title>Welcome | Nepal Reviewed</title>
</svelte:head>
<main class="section container p-0">
    <div class="hero has-background-success-light px-0 mx-0">
        <div class="hero-body ">
            <h1 class="title is-2 has-text-info-dark is-uppercase py-3">
                Nepal Reviewed
            </h1>
            <p class="subtitle is-7 is-italic has-text-success-dark py-2">
                Combining academic rigor and journalistic simplicity to produce
                knowledge for everyone
            </p>
        </div>
    </div>

    {#if $newPosts.length > 0}
        <article class="section container px-0 pt-1">
            <h2 class="title is-3 pl-3 has-text-centered">Latest</h2>
            <div class="container columns is-multiline  ">
                {#each $newPosts as post}
                    <PostItem {post} />
                {/each}
            </div>
        </article>
    {:else}
        <p>Posts on the way ...</p>
    {/if}
</main>
