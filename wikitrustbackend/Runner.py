from Firestore import Firestore
from WikiEngine import WikiEngine
import DiffEngine, ReputationEngine

f = Firestore()
w = WikiEngine()

# Get revs for title

# rev_list = w.get_revision_ids("HIV", 100) # ~99.4
rev_list = w.get_revision_ids("Stomach", 100)  # ~97.4 [0:1]
# rev_list = w.get_revision_ids("HIV", 100) # no change
# rev_list = w.get_revision_ids("Apple", 100) # no change


rev_a = w.get_revision_text(rev_list[0])
rev_b = w.get_revision_text(rev_list[1])


#Store article text
article_Stomach = {
    u"title": u"Stomach",
    u"text": rev_a,
}

f.writeArticle(str(rev_list[0]), article_Stomach)
art = f.readArticle(str(rev_list[0]))

# Compute diff
diff = DiffEngine.compute_edit_list(rev_a, rev_b)

# Compute rep from diff
parsed_diff = ReputationEngine.parseArray(str(diff))
rep = ReputationEngine.assignTrust(parsed_diff)

ReputationEngine.checkVal(parsed_diff, ReputationEngine.tArray)

#print ReputationEngine.tArray

print("rep: " + str(rep))

# Store data in db
id = str(rev_list[0]) + str(rev_list[1])
data = {u"diff_moves": str(diff), u"diff_trust": [1, 2, 3, 4], u"trust": rep}

f.writeDiff(id, data)

# make sure it stored
print(f.readDiff(id))
