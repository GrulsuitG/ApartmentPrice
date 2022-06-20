select t1.doro, t1.danginame, t1.buyyear, t1.buymonth, avg(t1.areadaprice) as areadaprice
from test.juso as t1, (select tt.doro, tt.buyyear, max(buymonth) as buymonth
						from (select t1.doro, t1.buyyear, t1.buymonth
						from test.juso t1, (select doro, max(buyyear) as max_year from test.juso group by doro) as t2
						where t1.doro = t2.doro and t1.buyyear = t2.max_year) as tt group by doro) as t3 
where t1.doro = t3.doro and t1.buyyear = t3.buyyear and t1.buymonth = t3.buymonth
group by t1.doro;