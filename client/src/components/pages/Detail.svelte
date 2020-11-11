<script>
    import { posts, postDetail } from "../../stores/postStore.js";
    import { push, pop, replace } from "svelte-spa-router";
    export let params = {};

    posts.subscribe((data) => {
        $postDetail = data.find((item) => item.id == params.id);
    });
</script>

<svelte:head>
    {#if $postDetail}
        <title>{$postDetail.title} | Nepal Reviewed</title>
    {/if}
</svelte:head>
{#if $postDetail}
    <div class="post container card ">
        {#if $postDetail.imageurl}
            <div class="card-image">
                <figure class="image is-4by3">
                    <img src={$postDetail.imageurl} alt="" />
                </figure>
            </div>
        {:else if $postDetail.image}
            <div class="card-image">
                <figure class="image is-4by3">
                    <img src={$postDetail.image} alt="" />
                </figure>
            </div>
        {/if}
        <div class="card-content">
            <p class="pb-1 is-size-6 is-italic has-text-grey">
                {new Date($postDetail.posted_date).toDateString()}
            </p>
            <h3 class="has-text-black">
                <a
                    href="#/categoryposts/{$postDetail.category}"
                    class="has-text-black is-capitalized">{$postDetail.category}</a>
            </h3>
            <h2 class="title">{$postDetail.title}</h2>
            <h3 class="pb-4 has-text-black has-text-weight-bold">
                {$postDetail.author}
            </h3>
            <div class="is-size-5">
                {@html $postDetail.content}
            </div>
            {#if $postDetail.review_item}
                <div class=" has-background-light has-text-grey ">
                    <p class="has-text-weight-bold p-2">
                        Review Item:
                        <span class="is-italic has-text-weight-normal">
                            {@html $postDetail.review_item}
                        </span>
                    </p>
                </div>
            {/if}

            <p>
                <span class="button is-small is-warning">Topics: </span>
                {#each $postDetail.topics as topic}
                    <a href="#/topicposts/{topic.name}">{topic.name} | </a>
                {/each}
            </p>
        </div>
    </div>
{/if}
