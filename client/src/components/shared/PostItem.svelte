<script>
    export let post;
</script>

<div class=" column is-half">
    <div class="m-1">
        <div class="card p-0 m-0">
            {#if post.imageurl}
                <div class="card-image">
                    <figure class="image is-4by3">
                        <img src={post.imageurl} alt="" />
                    </figure>
                </div>
            {:else if post.thumbnail}
                <div class="card-image">
                    <figure class="image is-4by3">
                        <img src={post.thumbnail} alt="" />
                    </figure>
                </div>
            {/if}

            <div class="post card-content">
                <p class="pb-1 is-size-7 is-italic has-text-grey">
                    {new Date(post.posted_date).toDateString()}
                    /
                    <a
                        href="#/categoryposts/{post.category}"
                        class="has-text-black">#{post.category}</a>
                </p>

                <h3 class="title">
                    <a
                        href="#/{post.id}/{post.category}/{post.slug}"
                        class="has-text-weight-bold has-text-dark is-size-3">{post.title}</a>
                </h3>
                <h4 class="has-text-weight-bold has-text-black pb-4">
                    {post.author}
                </h4>

                <p class="has-text-grey is-italic">
                    {post.summary.substring(0, 50)}
                    ...
                    <a
                        href="#/{post.id}/{post.category}/{post.slug}"
                        class="has-text-weight-bold is-link">Read full article</a>
                </p>

                <!-- <p>
                    <span class="button is-small is-warning">Topics: </span>

                    {#each post.topics as topic}
                        <a
                            href="#/topicposts/{topic.name}"
                            class=""
                            on:click>{topic.name}
                            |
                        </a>
                    {/each}
                </p> -->
            </div>
        </div>
    </div>
</div>
