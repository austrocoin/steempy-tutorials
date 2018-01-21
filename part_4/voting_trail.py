from steem import Steem
from steem.blockchain import Blockchain
from steem.post import Post

#create steem instance & pass it your private posting key
s = Steem(keys = ["<your private posting key>"])

#define trailing categories (tags)
tag = ["keyword1", "keyword2", "keyword3"]

voting_trail = ["amosbastian", "juliank"]
template = "@{}/{}"

steem = Steem()
blockchain = Blockchain()
stream = blockchain.stream(filter_by=["vote", "comment"])


if __name__ == '__main__':
    while True:
        try:
            for post in stream:
                postTags = post.json_metadata.get('tags', [])
            for vote in stream:
                voter = vote["voter"]
                author = vote["author"]
                permlink = vote["permlink"]

                if voter in voting_trail:
                    post = template.format(author, permlink)
                    postTags = post["tags"]
                    if Post(post).is_main_post() and tag in postTags:
                        print("Voting on {} post that {} voted on!".format(
                            permlink, voter))
                        steem.vote(post, 100)
                        print("... trailed with a 100% vote as used tag: {}".format(postTags)
                        
                        
                        
        except Exception as error:
            print("... NOT trailed because:")
            print(repr(error))
            continue
