%Adding Envelop to the monte-Carlo models;
load('TFA_Haw.mat')%T is total anomaly (induced +remanent) for 100 models;
load('x0_Haw.mat')%Observation points;
nNM = 100;%Number of Monte-Carlo models;
%Visualizing Monte-Carlo models;
%Tind = repmat(Tind,nNM,1);
for b = 1:nNM
   figure(9)
   plot(x0,T(b,:))
   hold on
end
nx0 = length(x0);
envelope1 = zeros(1,nx0);
envelope2 = zeros(1,nx0);
for i = 1:nx0
        envelope1(i) = 2*std(T(:,i));
        %envelope2(i) = -5*std(T(:,i));
end
open('HawaiiWithoutEnv.fig')%Anomaly fig for 25 Monte-Carlo Models;
hold on
plot(x0,envelope1,'--m')
%plot(x0,-3*envelope1,'--m')
%xlabel('Horizontal distance(km)','FontSize',28,'FontWeight','bold'),ylabel('Total Magnetic Anomaly(nT)','FontSize',28,'FontWeight','bold')
%title('Magnetic anomalies from Hawaii hotspot 460km Alt','FontSize',28,'FontWeight','bold')