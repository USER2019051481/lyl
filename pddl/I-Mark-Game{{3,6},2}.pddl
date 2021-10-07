(define (domain  i-mark-Game)
	(:objects ?v1)
	(:tercondition (or (=  ?v1 0) (=  ?v1 1)))
    (:constraint (>= ?v1 0))
    (:action take1
        :parameters (?k)
        :precondition (and (or (= ?k 3)  (= ?k 6))  (>= ?v1 ?k))
        :effect (assign ?v1 (- ?v1 ?k)))
    (:action take2
        :parameters (?k)
        :precondition (and (= ?v1 (+ ?k ?k)) (> ?v1 ?k))
        :effect (assign ?v1  ?k))
)