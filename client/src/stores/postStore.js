import { writable, derived } from "svelte/store";

export const posts = writable([]);

//posts for all pages --in sidebar
export const postTitles = derived(posts, ($posts) =>
  $posts.map((post) => {
    return {
      id: post.id,
      category: post.category,
      slug: post.slug,
      title: post.title,
    };
  }));
export const categoryPosts = writable ([])
export const topicPosts = writable([])
export const featuredPosts = writable([])
export const newPosts = writable([])
export const postDetail = writable({})

