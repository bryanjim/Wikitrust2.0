from Firestore import Firestore
from WikiEngine import WikiEngine
import DiffEngine, ReputationEngine

f = Firestore()
w = WikiEngine()

# Get revs for title
(rev_a, rev_b) = w.diff_revisions("Food")

# Compute diff
diff = DiffEngine.compute_edit_list(rev_a, rev_b)

# Compute rep from diff
parsed_diff = ReputationEngine.parseArray(str(diff))
rep = ReputationEngine.assignTrust(parsed_diff)
rep = 1

print "rep: " + str(rep)

# Store data in db
id = '12334'
data = {
    u'diff_moves': str(diff),
    u'diff_trust': [1,2,3,4],
    u'trust': rep
}

f.writeDiff(id, data)

# make sure it stored
print f.readDiff(id)