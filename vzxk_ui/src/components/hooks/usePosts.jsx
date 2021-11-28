import {useMemo} from "react";

export const useSortedPosts = (posts, sort) => {
    const sortedPost = useMemo(()=>{
        if (sort) {
            return [...posts].sort((a,b)=> a[sort].localeCompare(b[sort]))
        }
        return posts
    }, [sort, posts])
    return sortedPost
}  

export const usePosts = (posts, sort, query) => {
    const sortedPost = useSortedPosts(posts, sort)
    const getSortedandFilteredList = useMemo(()=>{
        return sortedPost.filter(post => post.first_name.toLowerCase().includes(query))
    }, [query, sortedPost])
    return getSortedandFilteredList
}