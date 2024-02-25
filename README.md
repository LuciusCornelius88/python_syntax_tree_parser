# syntax_tree_parser

A console project to parse the syntax trees and find different acceptable syntax combinations.

**Idea**

To achieve uniqueness in the description of the historical district of Barcelona for your online guide, you can utilize a paraphrasing microservice that can rephrase the text without altering its meaning. Here's an example of how you might transform a sentence using such a service:

Original sentence: "The historic district of Barcelona is known for its charming narrow streets and iconic architecture."

Paraphrased sentence: "Barcelona's historic area is famous for its quaint winding streets and distinctive architectural landmarks."

Using a paraphrasing microservice, you can generate multiple unique versions of your description while maintaining the core information intact. This can help ensure that your content stands out and avoids duplication when competing for visibility in search engine rankings.

**Implementation**

The script uses the nltk module to anayze the syntax trees and build the variations of it.

**Example**

The following input: (S(NP(NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter))(, ,)(CC or)(NP (NNP Barri) (NNP Gòtic)))(, ,)(VP(VBZ has)(NP(NP (JJ narrow) (JJ medieval) (NNS streets))(VP(VBN filled)(PP(IN with)(NP(NP (JJ trendy) (NNS bars))(, ,)(NP (NNS clubs))(CC and)(NP (JJ Catalan)(NNS restaurants))))))))

will result in the set of paraphrases:

1. (S(NP(NP(DTThe)(JJcharming)(NNPGothic)(NNPQuarter))(,,)(CCor)(NP(NNPBarri)(NNPGòtic)))(,,)(VP(VBZhas)(NP(NP(JJnarrow)(JJmedieval)(NNSstreets))(VP(VBNfilled)(PP(INwith)(NP(NP(JJtrendy)(NNSbars))(,,)(NP(NNSclubs))(CCand)(NP(JJCatalan)(NNSrestaurants))))))))

2. (S(NP(NP(DTThe)(JJcharming)(NNPGothic)(NNPQuarter))(,,)(CCor)(NP(NNPBarri)(NNPGòtic)))(,,)(VP(VBZhas)(NP(NP(JJnarrow)(JJmedieval)(NNSstreets))(VP(VBNfilled)(PP(INwith)(NP(NP(JJtrendy)(NNSbars))(,,)(NP(JJCatalan)(NNSrestaurants))(CCand)(NP(NNSclubs))))))))

3. (S(NP(NP(DTThe)(JJcharming)(NNPGothic)(NNPQuarter))(,,)(CCor)(NP(NNPBarri)(NNPGòtic)))(,,)(VP(VBZhas)(NP(NP(JJnarrow)(JJmedieval)(NNSstreets))(VP(VBNfilled)(PP(INwith)(NP(NP(NNSclubs))(,,)(NP(JJtrendy)(NNSbars))(CCand)(NP(JJCatalan)(NNSrestaurants))))))))

4. (S(NP(NP(DTThe)(JJcharming)(NNPGothic)(NNPQuarter))(,,)(CCor)(NP(NNPBarri)(NNPGòtic)))(,,)(VP(VBZhas)(NP(NP(JJnarrow)(JJmedieval)(NNSstreets))(VP(VBNfilled)(PP(INwith)(NP(NP(NNSclubs))(,,)(NP(JJCatalan)(NNSrestaurants))(CCand)(NP(JJtrendy)(NNSbars))))))))

5. (S(NP(NP(DTThe)(JJcharming)(NNPGothic)(NNPQuarter))(,,)(CCor)(NP(NNPBarri)(NNPGòtic)))(,,)(VP(VBZhas)(NP(NP(JJnarrow)(JJmedieval)(NNSstreets))(VP(VBNfilled)(PP(INwith)(NP(NP(JJCatalan)(NNSrestaurants))(,,)(NP(JJtrendy)(NNSbars))(CCand)(NP(NNSclubs))))))))
