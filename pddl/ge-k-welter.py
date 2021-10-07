import os

def generate(k,v2max):
    k=str(k)
    v2max=str(v2max)
    filename = os.path.dirname(__file__)+'\\'+k+'-wythoffGamel(v2le'+v2max+').pddl'
    print(filename)
    content='''
(define (domain a-Wythoff_game)
    (:objects ?v1 ?v2)
    (:tercondition (and (= ?v1 0) (= ?v2 0)))
    (:constraint (and (>= ?v1 0) (>= ?v2 0) (<= ?v2 %s)))
    (:action take1
        :parameters (?k)
        :precondition (and (>= ?v1 ?k) (> ?k 0))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (>= ?v2 ?k) (> ?k 0))
        :effect (assign ?v2 (- ?v2 ?k)))
    (:action take3
        :parameters (?k ?l)
        :precondition (and (>= ?v1 ?k) (> ?k 0) (>= ?v2 ?l) (> ?l 0)  (or (and (< (- ?k ?l) %s) (>= ?k ?l)) (and (< (- ?l ?k) %s) (>=  ?l ?k))))
        :effect (and (assign ?v1 (- ?v1 ?k)) (assign ?v2 (- ?v2 ?l))))
)
    '''%(v2max,k,k)
    fp = open(filename,'w') 

    fp.write(content)

    fp.close()
    return

for k in range (1,6):
    for j in range(0,6):
        generate(k,j)
# generate(1,1)