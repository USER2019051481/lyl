(define (domain Empty-and-Transfer)
	(:objects ?v1 ?v2 ?v3)
	(:tercondition (and (= ?v1 1) (= ?v2 1) (= ?v3 1)))
    (:constraint (and (>= ?v1 1) (>= ?v2 1) (= ?v3 1)))
    (:action empty1
        :parameters (?k ?k1)
        :precondition (and (or (and (= ?k1 2) (> ?v2 ?k)) (and (= ?k1 3) (> ?v3 ?k)) ) (> ?k 0))
        :effect (and (assign ?v1  ?k) (when (= ?k1 2) (assign ?v2 (- ?v2 ?k)))  (when (= ?k1 3) (assign ?v3 (- ?v3 ?k)))))
    (:action empty2
        :parameters (?k ?k1)
        :precondition (and (or (and (= ?k1 1) (> ?v1 ?k)) (and (= ?k1 3) (> ?v3 ?k)) ) (> ?k 0))
        :effect (and (assign ?v2  ?k) (when (= ?k1 1) (assign ?v1 (- ?v1 ?k)))  (when (= ?k1 3) (assign ?v3 (- ?v3 ?k)))))
    (:action empty3
        :parameters (?k ?k1)
        :precondition (and (or (and (= ?k1 2) (> ?v2 ?k)) (and (= ?k1 1) (> ?v1 ?k)) ) (> ?k 0))
        :effect (and (assign ?v3  ?k) (when (= ?k1 2) (assign ?v2 (- ?v2 ?k))) (when (= ?k1 1) (assign ?v1 (- ?v1 ?k)))))
)